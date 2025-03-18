import os
import git
from dataclasses import dataclass, fields, asdict
from typing import Tuple, Dict, Any, Optional
from ansible.module_utils.basic import AnsibleModule

@dataclass
class GitModuleArgs:
    repo_path: str
    commit_message: str

    @classmethod
    def to_argument_spec(cls) -> Dict[str, Dict[str, Any]]:
        """Convert dataclass fields into AnsibleModule argument_spec.
     Arguments without default values are required """
        return {f.name: {"type": "str", "required": f.default is None} for f in fields(cls)}

@dataclass
class AnsibleModResponse:
    changed: bool = False
    failed: bool = False
    msg: str = ""

    def to_dict(self) -> Dict[str, Any]:
        """Convert response to dictionary format for Ansible."""
        return asdict(self)

def is_repo_exist(repo_path: str) -> bool:
    """Check if .git directory exists."""
    return os.path.exists(os.path.join(repo_path, ".git"))

def init_repo(repo_path: str) -> Tuple[Optional[git.Repo], AnsibleModResponse]:
    """Initialize or open a Git repository and return (repo, response)."""
    try:
        if is_repo_exist(repo_path):
            repo = git.Repo(repo_path)
            return repo, AnsibleModResponse(changed=False, msg="Opened existing repo")
        else:
            repo = git.Repo.init(repo_path)
            return repo, AnsibleModResponse(changed=True, msg="Initialized new repo")
    except Exception as e:
        return None, AnsibleModResponse(failed=True, msg=f"Git operation failed: {str(e)}")

def commit_repo(repo: Optional[git.Repo], commit_message: str) -> AnsibleModResponse:
    """Stage, commit, and return commit status."""
    if repo is None:
        return AnsibleModResponse(failed=True, msg="Cannot commit: Repository is None")

    try:
        repo.git.add(A=True)
        if repo.is_dirty(untracked_files=True):
            repo.index.commit(commit_message)
            return AnsibleModResponse(changed=True, msg=f"Successfully committed: {commit_message}")
        return AnsibleModResponse(changed=False, msg="Nothing to commit")
    except Exception as e:
        return AnsibleModResponse(failed=True, msg=f"Commit failed: {str(e)}")

def main():
    module_args = GitModuleArgs.to_argument_spec()
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    params = GitModuleArgs(**module.params)

    repo, init_response = init_repo(params.repo_path)
    if init_response.failed:
        module.fail_json(**init_response.to_dict())

    commit_response = commit_repo(repo, params.commit_message)
    if commit_response.failed:
        module.fail_json(**commit_response.to_dict())

    module.exit_json(**commit_response.to_dict())

if __name__ == "__main__":
    main()

