from pyinfra.modules import brew, pip, server


brew.casks(
    {'Install brew cask apps'},
    [
        'aerial',
        'android-file-transfer',
        'android-platform-tools',
        'appcleaner',
        'bartender',  # show/hide groups of menu bar apps
        'coconutbattery',
        'disk-inventory-x',
        'docker',
        'dropbox',
        'fantastical',
        'firefox',
        'forklift'
        'istumbler',
        'iterm2',
        'intel-power-gadget',
        'java',
        'keepassx',  # TODO: remove this? (keepassxc)
        'keepassxc',
        'little-snitch',
        'macs-fan-control',
        'pyenv',
        'pyenv-virtualenv',
        'sequel-pro',
        'slack',
        'spectacle',
        'spotify',
        'standard-notes',
        'sublime-text',
        'transmission',
        'tunnelblick',
        'vagrant',
        'virtualbox',
        'vlc',
        'youtube-to-mp3',
    ],
)

brew.packages(
    {'Install brew packages'},
    [
        'bash',
        'bash-completion',
        'coreutils',
        'curl',
        'git',
        'git-lfs',
        'gnupg',
        'htop',
        'libffi',
        'lua',
        'mtr',
        'node',
        'pandoc',
        'pinentry-mac',
        'python',
        'python3',
        'smartmontools',
        'tinc',
        'yarn',
        'watch',
    ],
)

server.shell(
    {'Install Python 3.8.0 with pyenv'},
    'pyenv install 3.8.0',
    env={
        'PYTHON_CONFIGURE_OPTS': '--enable-framework',
    },
)

pip.packages(
    {'Install pip packages'},
    ['virtualenv', 'pyinfra', 'ansible'],
)
