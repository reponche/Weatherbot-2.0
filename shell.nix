let
  pkgs = import <nixpkgs> {};
  python-deps = python-packages: with python-packages; [
    pyyaml
    requests
  ];
  python-with-deps = pkgs.python37.withPackages python-deps;
in
pkgs.stdenv.mkDerivation rec {
  name = "weather";

  # The packages in the `buildInputs` list will be added to the PATH in our shell
  buildInputs = [
    pkgs.jq 
    python-with-deps

    pkgs.figlet
  ];

  shellHook = ''
    export NIX_NAME='' + name + '' && figlet $NIX_NAME
  '';
}
