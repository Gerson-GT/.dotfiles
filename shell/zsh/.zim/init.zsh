zimfw() { source /home/gerson/.dotfiles/shell/zsh/.zim/zimfw.zsh "${@}" }
zmodule() { source /home/gerson/.dotfiles/shell/zsh/.zim/zimfw.zsh "${@}" }
fpath=(/home/gerson/.dotfiles/shell/zsh/.zim/modules/git-info/functions ${fpath})
autoload -Uz -- coalesce git-action git-info
source /home/gerson/.dotfiles/shell/zsh/.zim/modules/environment/init.zsh
source /home/gerson/.dotfiles/shell/zsh/.zim/modules/input/init.zsh
source /home/gerson/.dotfiles/shell/zsh/.zim/modules/completion/init.zsh
source /home/gerson/.dotfiles/shell/zsh/.zim/modules/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /home/gerson/.dotfiles/shell/zsh/.zim/modules/zsh-autosuggestions/zsh-autosuggestions.zsh
