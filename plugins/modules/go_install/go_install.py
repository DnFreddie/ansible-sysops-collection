#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule
import shutil
import subprocess
from typing import Dict


def isPkgAvailable(pkg_name: str) -> bool:
    """Check if the given package or binary is available in the system's PATH."""
    return shutil.which(pkg_name) is not None


def getPkgName(pkg_url: str) -> str:
    """Extract the package name from a Go package URL, ignoring versions or suffixes."""
    last_segment = pkg_url.split("/")[-1]
    pkg_name = last_segment.split("@")[0]
    return pkg_name


def go_install(pkg: str) -> Dict[str, str]:
    """Attempt to install a Go package and return a dictionary with the result."""
    try:
        subprocess.run(
            ["go", "install", pkg], check=True, text=True, capture_output=True
        )
        return {"package": pkg, "status": "installed"}
    
    except subprocess.CalledProcessError as e:
        return {"package": pkg, "status": "failed", "error": e.stderr.strip()}


def runModule():
    module_args = {"go_pkg": {"type": "str", "required": True}}

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)
    params = module.params

    go_pkg: str = params["go_pkg"]

    pkg_name = getPkgName(go_pkg)

    if isPkgAvailable(pkg_name):
        module.exit_json(changed=False, msg=f"{pkg_name} is already installed")

    if not isPkgAvailable("go"):
        module.fail_json(msg="Failed to find 'go' on the system")

    installation_result = go_install(go_pkg)

    failed = installation_result["status"] == "failed"

    module.exit_json(changed=not failed, results=installation_result, failed=failed)


if __name__ == "__main__":
    runModule()

