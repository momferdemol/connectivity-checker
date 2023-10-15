
<pre>
  Title: URL Connectivity Checker
  Author: Momfer de Mol
  Status: WIP
  Created: 15-10-2023
</pre>

## Connectivity Checker

Program help
```sh
$ python -m epchecker -h
```

Run program
```sh
$ python -m epchecker -u www.foobar.com
```

```sh
$ python -m epchecker -f endpoints.txt
```

**Dependency**

Python dependencies are listed in `pyproject.toml` and installed with poetry.

**Environment**

Use environment variable `LOGGEL_LVL` to set the logger level (INFO, WARNING, DEBUG etc.).

Set environment variable `DEBUG` is `True` to display trace back.

**Development**

Local development environment created with `devenv.nix`.