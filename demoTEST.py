class MyObj():
    def __init__(self, repo):
        self._repo = repo
        repo.connect("hello")

    def setup(self):
        self._repo.setup(cache=True)