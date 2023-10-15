{ pkgs, config, ... }:

{
  # devenv debug mode
  devenv.debug = false;

  # environment variables
  env.LOGGER_LEVEL = "INFO";
  # env.DEBUG = "True";
  env.GREET = "---->> hello! ready to code?";
  env.VERSIONS = "---->> versions";

  # cross-shell prompt
  starship.enable = true;

  # language support
  languages.python = {
    enable = true;
    version = "3.10";
    poetry.enable = true;
    poetry.activate.enable = true;
    poetry.install.enable = true;
  };

  # hello script
  scripts.hello.exec = "echo $GREET";

  # echo versions
  scripts.versions.exec = "
    echo $VERSIONS
    echo
    git --version
    python --version
    poetry --version
  ";

  # run processes ($ devenv up)
  processes = {
      bot.exec = "python app";
    };

  # enter devenv shell
  enterShell = ''
    echo
    versions
    echo
    hello
    echo
  '';

  # See full devenv reference at https://devenv.sh/reference/options/
}
