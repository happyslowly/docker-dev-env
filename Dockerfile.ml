from xixu/dev-base:latest

user root

run pacman -Syy
run pacman -S --noconfirm \
    python-pandas python-numpy python-scikit-learn ipython jupyter

user xixu
