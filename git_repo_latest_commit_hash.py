import sys

from git import Repo


# w argumencie podajemy ścieżkę do folderu, gdzie znajduje się repozytorium
def get_git_commit_hash(repo_path="."):

    try:
        # tworzę obiekt typu Repo aby móc operować na repo wskazywanym przez repo_path
        repo = Repo(repo_path)
    except:
        # Jeżeli pliki leżą w folderze nie należącym do repozytorium git, należy użyć wartości "unknown"
        print("Nie można było otworzyć repozytorium pod wskazanym adresem")
        return "unknown"


    # pobieram nazwę aktywnego brancha
    branch_name = repo.active_branch
    print('Repozytorium działa na branchu: {}'.format(branch_name))

    # pobieram hash ostatniego commita
    commit_hash = list(repo.iter_commits(branch_name))[0].hexsha
    print('Hash ostatniego commita: {}'.format(commit_hash))
    return commit_hash


if __name__ == "__main__":
    get_git_commit_hash(sys.argv[1])

