# Feedback and Contribution

We welcome any input, feedback, bug reports, and contributions.

All contributions, suggestions, and feedback you submitted are accepted under the [Project's license](./LICENSE.md). You represent that if you do not own copyright in the code that you have the authority to submit it under the [Project's license](./LICENSE.md). All feedback, suggestions, or contributions are not confidential. The Project abides by the [code of conduct](https://github.com/vega/.github/blob/main/CODE_OF_CONDUCT.md).

## How To Contribute Code

### Setting Up Your Environment

Fork the Altair repository on GitHub and then clone the fork to you local
machine. For more details on forking see the [GitHub
Documentation](https://help.github.com/en/articles/fork-a-repo).

```cmd
git clone git@github.com:UBC-MDS/group-2.git
```

To keep your fork up to date with changes in this repo,
you can [use the fetch upstream button on GitHub](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork).

Now you can install the conda environment.

```cmd
conda env create --file environment.yml
conda activate 522
```

### Creating a Branch

Once your local environment is up-to-date, you can create a new git branch
which will contain your contribution
(always create a new branch instead of making changes to the main branch):

```cmd
git switch -c <your-branch-name>
```

With this branch checked-out, make the desired changes to the package.

A large part of Altair's code base is automatically generated.
After you have made your manual changes,
make sure to run the following to see if there are any changes
to the automatically generated files: 

```bash
hatch run generate-schema-wrapper
```

For information on how to update the Vega-Lite version that Altair uses,
please read [the maintainers' notes](NOTES_FOR_MAINTAINERS.md).

### Testing your Changes

Before submitting your changes to the main Altair repository,
it is recommended that you run the Altair test suite,
which includes a number of tests to validate the correctness of your code:

```bash
hatch test
```


This also runs the [`ruff`](https://ruff.rs/) linter and formatter as well as [`mypy`](https://mypy-lang.org/) as type checker.


Study the output of any failed tests and try to fix the issues
before proceeding to the next section.

#### Failures on specific python version(s)
By default, `hatch test` will run the test suite against the currently active python version.
Two useful variants for debugging failures that only appear *after* you've submitted your PR:

```bash
# Test against all python version(s) in the matrix
hatch test --all
# Test against a specific python version
hatch test --python 3.8
```

See [hatch test](https://hatch.pypa.io/latest/cli/reference/#hatch-test) docs for other options.

#### Changes to `__all__`
If `test_completeness_of__all__` fails, you may need to run:

```bash
hatch run update-init-file
```
However, this test usually indicates *unintentional* addition(s) to the top-level `alt.` namespace that will need resolving first.

### Creating a Pull Request

When you are happy with your changes, you can commit them to your branch by running

```cmd
git add <modified-file>
git commit -m "Some descriptive message about your change"
git push origin <your-branch-name>
```

You will then need to submit a pull request (PR) on GitHub asking to merge
your example branch into the main Altair repository. For details on creating a PR see GitHub
documentation [Creating a pull
request](https://help.github.com/en/articles/creating-a-pull-request). You can
add more details about your example in the PR such as motivation for the
example or why you thought it would be a good addition.  You will get feed back
in the PR discussion if anything needs to be changed. To make changes continue
to push commits made in your local example branch to origin and they will be
automatically shown in the PR. 

Hopefully your PR will be answered in a timely manner and your contribution will
help others in the future.

## How To Contribute Documentation

-to be determined-

---

Part of MVG-0.1-beta.
Made with love by GitHub. Licensed under the [CC-BY 4.0 License](https://creativecommons.org/licenses/by-sa/4.0/).
