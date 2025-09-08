# My Dotfiles ⚙️

These are my personal configuration files for building a productive and beautiful shell environment. The setup is managed using a bare Git repository technique.

![](https://user-images.githubusercontent.com/penzulo/repo/branch/screenshot.png)
*(A screenshot of your prompt is a great addition here!)*

---

### ## Contents

This repository currently manages configurations for:
* **Shell:** [Nushell](https://www.nushell.sh/)
* **Prompt:** [Starship](https://starship.rs/)
* **Editor:** [Neovim](https://neovim.io/) *(Add this when you add your nvim config)*
* ...and more to come!

---

### ## Installation

To set this up on a new machine, follow these steps:

1.  **Clone the repository:**
    ```nu
    git clone --bare https://github.com/penzulo/dotfiles.git $"($env.USERPROFILE)/.dotfiles"
    ```

2.  **Define the alias:**
    Add the following alias to your shell's configuration file (e.g., `.bashrc`, `.zshrc`, or `config.nu` if you're bootstrapping Nushell).
    ```nu
    alias dotgit = git --git-dir $"($env.USERPROFILE)\.dotfiles" --work-tree $env.USERPROFILE
    ```

3.  **Check out the files:**
    Source your shell config or open a new terminal, then run the checkout command. You may need to stash existing default files if they conflict.
    ```nu
    # Checkout the contents from the repo into your home directory
    dotgit checkout

    # If the above command fails due to existing files, force the checkout.
    # WARNING: This will overwrite existing files.
    dotgit checkout -f
    ```

4.  **Set the `showUntrackedFiles` flag:**
    Configure the local repository to hide untracked files in its status.
    ```sh
    dotgit config --local status.showUntrackedFiles no
    ```

You are now ready to go!
