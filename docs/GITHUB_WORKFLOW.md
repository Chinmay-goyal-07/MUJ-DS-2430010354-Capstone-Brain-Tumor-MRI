# GitHub Workflow

## Branching

- `main`: always working; changes arrive only through reviewed pull requests.
- Feature branches: `feature/<short-name>`, `docs/<short-name>`, `fix/<short-name>`, `test/<short-name>`.
- One branch per issue. Name it after the issue, e.g. `feature/12-model-evaluation`.

## Steps for every change

1. Pick (or create) an issue and assign yourself.
2. `git checkout main && git pull`
3. `git checkout -b feature/<short-name>`
4. Make small, focused commits with clear messages (`Add 5-fold CV loop`, not `update`).
5. `git push -u origin feature/<short-name>`
6. Open a pull request, link the issue with `Closes #<number>`, and request a review from a teammate.
7. The reviewer leaves comments or approves. Address feedback with more commits.
8. Merge after approval (squash or merge commit; the team picks one and sticks with it).
9. Delete the merged branch.

## Rules

- Nobody merges their own pull request without a teammate's review.
- Do not commit the dataset or `.pt` model files. Share them through a download link in the README.
- Push regularly; GitHub activity should be continuous across the training period, not one large final commit.
- Every team member and the instructor must be a collaborator on this repository.

## Commit message style

`<verb> <what>`: e.g. `Add confusion matrix plot`, `Fix class order check`, `Document Colab setup`.
