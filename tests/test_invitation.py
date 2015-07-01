# coding: utf-8
from .suite import BaseSuite


class TestInvitation(BaseSuite):
    def test_action(self):
        rv = self.client.get('/invitation/action')
        assert rv.status_code == 200
