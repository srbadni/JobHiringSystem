from application.common.ports.unit_of_work import UnitOfWork
from application.jobs_search.dto.company_details import CompanyDetails
from application.jobs_search.ports.jobs_search_repository import GetCompanyDetailsQueries
from application.jobs_search.query.get_company_details import GetCompanyDetailsQuery


class GetCompanyDetailsHandler:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def handle(self, query: GetCompanyDetailsQuery) -> CompanyDetails:
        async with self.uow:
            return await self.uow.jobs_search.get_company_details(
                GetCompanyDetailsQueries(company_en_name=query.company_en_name)
            )
