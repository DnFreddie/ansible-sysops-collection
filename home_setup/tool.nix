{pkgs, ...}: {
    home.username = "proxy";
    home.homeDirectory = "/home/proxy";
    home.stateVersion = "22.11"; 
    programs.home-manager.enable = true;
    home.packages = with pkgs; [
            neovim 
            bat
            fzf
            nmap




            ];

}




















