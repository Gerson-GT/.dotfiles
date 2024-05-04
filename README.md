<h1 align="center">
  .dotfiles created using <a href="https://github.com/CodelyTV/dotly">🌚 dotly</a>
</h1>


<h1 align="center">
  Programs to install
</h1>

* Git
* Curl
* <a href="https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH"> ZSH</a>
* <a href="https://www.rust-lang.org/tools/install"> Rust</a>
* <a href="https://alacritty.org/"> Alacritty</a>
* Vim and Neovim
* <a href="https://github.com/zimfw/zimfw"> Zim</a>
* <a href="https://forums.linuxmint.com/viewtopic.php?t=231902"> Mount NTFS data</a>

## Restore your Dotfiles manually

* Install git
* Clone your dotfiles repository `git clone [your repository of dotfiles] $HOME/.dotfiles`
* Go to your dotfiles folder `cd $HOME/.dotfiles`
* Install git submodules `git submodule update --init --recursive modules/dotly`
* Install your dotfiles `DOTFILES_PATH="$HOME/.dotfiles" DOTLY_PATH="$DOTFILES_PATH/modules/dotly" "$DOTLY_PATH/bin/dot" self install`
* Restart your terminal
* Import your packages `dot package import`

## Restore your Dotfiles with script

Using wget
```bash
bash <(wget -qO- https://raw.githubusercontent.com/CodelyTV/dotly/HEAD/restorer)
```

Using curl
```bash
bash <(curl -s https://raw.githubusercontent.com/CodelyTV/dotly/HEAD/restorer)
```

You need to know your GitHub username, repository and install ssh key if your repository is private.

It also supports other git repos, but you need to know your git repository url.
