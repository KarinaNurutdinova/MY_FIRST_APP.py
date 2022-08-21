from app.vacancies.dao.vacancies_dao import VacanciesDAO
import pytest

keys_should_be = {"pk", "company", "position", "salary"}


@pytest.fixture()
def vacancies_dao():
    vacancies_dao_instance = VacanciesDAO("./data/vacancies.json")
    return vacancies_dao_instance


class TestVacanciesDAO:

    def test_get_all(self, vacancies_dao):
        vacancies = vacancies_dao.get_all()
        assert type(vacancies) == list,"возвращается не список"
        assert len(vacancies) > 0, "возвращается пустой список"
        assert set(vacancies[0].keys()) == keys_should_be, "неверный список ключей"

    def test_get_by_pk(self, vacancies_dao):
        vacancy = vacancies_dao.get_by_pk(1)
        assert type(vacancy) == dict, "возвращается не словарь"
        assert vacancy["pk"] == 1, "возвращается неправильная вакансия"
        assert set(vacancy.keys()) == keys_should_be, "неверный список ключей"
