from app.candidates.dao.candidates_dao import CandidateDAO

import pytest


@pytest.fixture()
def candidates_dao():
    candidates_dao_instance = CandidateDAO("./data/candidates.json")
    return candidates_dao_instance


keys_should_be = {"pk", "name", "position"}


class TestCandidatesDAO:

    def test_get_all(self, candidates_dao):
        candidates = candidates_dao.get_all()
        assert type(candidates) == list, "возвращается не список"
        assert len(candidates) > 0, "возвращается пустой список"
        assert set(candidates[0].keys()) == keys_should_be, "неверный список ключей"

    def test_get_by_id(self, candidates_dao):
        """ Проверяем, верный ли кандидат возвращается при запросе одного """
        candidate = candidates_dao.get_by_pk(1)
        assert candidate["pk"] == 1, "возвращается неправильный кандидат"
        assert set(candidate.keys()) == keys_should_be, "неверный список ключей"
