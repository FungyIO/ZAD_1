import os
from git import Repo


# w argumencie podajemy ścieżkę do folderu, gdzie znajduje się repozytorium
def get_git_commit_hash(directory_path):
    repo_path = directory_path

    try:
        # tworzę obiekt typu Repo aby móc operować na repo wskazywanym przez repo_path
        repo = Repo(repo_path)

        # sprawdzam, czy repozytorium załadowało się poprawnie
        if not repo.bare:

            # pobieram nazwę aktywnego brancha
            branch_name = repo.active_branch
            print('Repozytorium działa na branchu: {}'.format(branch_name))

            commit_hash = list(repo.iter_commits('master'))[0].hexsha
            print(commit_hash)

    except:
        # Jeżeli pliki leżą w folderze nie należącym do repozytorium git, należy użyć wartości "unknown"
        print("Nie można było otworzyć repozytorium pod wskazanym adresem")
        return "unknown"


if __name__ == "__main__":
    get_git_commit_hash(".")
