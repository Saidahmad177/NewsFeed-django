from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class PermissionUser(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class OnlyLoggedSuperUser(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser
