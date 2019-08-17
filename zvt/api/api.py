
# -*- coding: utf-8 -*-
from typing import List, Union

import pandas as pd
from sqlalchemy.orm import Session
from zvdata.api import get_data
from zvdata.structs import IntervalLevel

from zvt.domain import HolderTrading

def get_holder_trading(
        entity_ids: List[str] = None,
        entity_id: str = None,
        codes: List[str] = None,
        level: Union[IntervalLevel, str] = None,
        provider: str = 'eastmoney',
        columns: List = None,
        return_type: str = 'df',
        start_timestamp: Union[pd.Timestamp, str] = None,
        end_timestamp: Union[pd.Timestamp, str] = None,
        filters: List = None,
        session: Session = None,
        order=None,
        limit: int = None,
        index: str = 'timestamp',
        index_is_time: bool = True,
        time_field: str = 'timestamp'):
    return get_data(data_schema=HolderTrading, entity_ids=entity_ids, entity_id=entity_id, codes=codes, level=level,
                    provider=provider,
                    columns=columns, return_type=return_type, start_timestamp=start_timestamp,
                    end_timestamp=end_timestamp, filters=filters, session=session, order=order, limit=limit,
                    index=index, index_is_time=index_is_time, time_field=time_field)


from zvt.domain import IndexMoneyFlow

def get_index_money_flow(
        entity_ids: List[str] = None,
        entity_id: str = None,
        codes: List[str] = None,
        level: Union[IntervalLevel, str] = None,
        provider: str = 'sina',
        columns: List = None,
        return_type: str = 'df',
        start_timestamp: Union[pd.Timestamp, str] = None,
        end_timestamp: Union[pd.Timestamp, str] = None,
        filters: List = None,
        session: Session = None,
        order=None,
        limit: int = None,
        index: str = 'timestamp',
        index_is_time: bool = True,
        time_field: str = 'timestamp'):
    return get_data(data_schema=IndexMoneyFlow, entity_ids=entity_ids, entity_id=entity_id, codes=codes, level=level,
                    provider=provider,
                    columns=columns, return_type=return_type, start_timestamp=start_timestamp,
                    end_timestamp=end_timestamp, filters=filters, session=session, order=order, limit=limit,
                    index=index, index_is_time=index_is_time, time_field=time_field)


from zvt.domain import Index

def get_indices(
        entity_ids: List[str] = None,
        entity_id: str = None,
        codes: List[str] = None,
        level: Union[IntervalLevel, str] = None,
        provider: str = 'exchange',
        columns: List = None,
        return_type: str = 'df',
        start_timestamp: Union[pd.Timestamp, str] = None,
        end_timestamp: Union[pd.Timestamp, str] = None,
        filters: List = None,
        session: Session = None,
        order=None,
        limit: int = None,
        index: str = 'timestamp',
        index_is_time: bool = True,
        time_field: str = 'timestamp'):
    return get_data(data_schema=Index, entity_ids=entity_ids, entity_id=entity_id, codes=codes, level=level,
                    provider=provider,
                    columns=columns, return_type=return_type, start_timestamp=start_timestamp,
                    end_timestamp=end_timestamp, filters=filters, session=session, order=order, limit=limit,
                    index=index, index_is_time=index_is_time, time_field=time_field)


from zvt.domain import DragonAndTiger

def get_dragon_and_tiger(
        entity_ids: List[str] = None,
        entity_id: str = None,
        codes: List[str] = None,
        level: Union[IntervalLevel, str] = None,
        provider: str = 'eastmoney',
        columns: List = None,
        return_type: str = 'df',
        start_timestamp: Union[pd.Timestamp, str] = None,
        end_timestamp: Union[pd.Timestamp, str] = None,
        filters: List = None,
        session: Session = None,
        order=None,
        limit: int = None,
        index: str = 'timestamp',
        index_is_time: bool = True,
        time_field: str = 'timestamp'):
    return get_data(data_schema=DragonAndTiger, entity_ids=entity_ids, entity_id=entity_id, codes=codes, level=level,
                    provider=provider,
                    columns=columns, return_type=return_type, start_timestamp=start_timestamp,
                    end_timestamp=end_timestamp, filters=filters, session=session, order=order, limit=limit,
                    index=index, index_is_time=index_is_time, time_field=time_field)


from zvt.domain import BalanceSheet

def get_balance_sheet(
        entity_ids: List[str] = None,
        entity_id: str = None,
        codes: List[str] = None,
        level: Union[IntervalLevel, str] = None,
        provider: str = 'eastmoney',
        columns: List = None,
        return_type: str = 'df',
        start_timestamp: Union[pd.Timestamp, str] = None,
        end_timestamp: Union[pd.Timestamp, str] = None,
        filters: List = None,
        session: Session = None,
        order=None,
        limit: int = None,
        index: str = 'timestamp',
        index_is_time: bool = True,
        time_field: str = 'timestamp'):
    return get_data(data_schema=BalanceSheet, entity_ids=entity_ids, entity_id=entity_id, codes=codes, level=level,
                    provider=provider,
                    columns=columns, return_type=return_type, start_timestamp=start_timestamp,
                    end_timestamp=end_timestamp, filters=filters, session=session, order=order, limit=limit,
                    index=index, index_is_time=index_is_time, time_field=time_field)


from zvt.domain import RightsIssueDetail

def get_rights_issue_detail(
        entity_ids: List[str] = None,
        entity_id: str = None,
        codes: List[str] = None,
        level: Union[IntervalLevel, str] = None,
        provider: str = 'eastmoney',
        columns: List = None,
        return_type: str = 'df',
        start_timestamp: Union[pd.Timestamp, str] = None,
        end_timestamp: Union[pd.Timestamp, str] = None,
        filters: List = None,
        session: Session = None,
        order=None,
        limit: int = None,
        index: str = 'timestamp',
        index_is_time: bool = True,
        time_field: str = 'timestamp'):
    return get_data(data_schema=RightsIssueDetail, entity_ids=entity_ids, entity_id=entity_id, codes=codes, level=level,
                    provider=provider,
                    columns=columns, return_type=return_type, start_timestamp=start_timestamp,
                    end_timestamp=end_timestamp, filters=filters, session=session, order=order, limit=limit,
                    index=index, index_is_time=index_is_time, time_field=time_field)


from zvt.domain import CashFlowStatement

def get_cash_flow_statement(
        entity_ids: List[str] = None,
        entity_id: str = None,
        codes: List[str] = None,
        level: Union[IntervalLevel, str] = None,
        provider: str = 'eastmoney',
        columns: List = None,
        return_type: str = 'df',
        start_timestamp: Union[pd.Timestamp, str] = None,
        end_timestamp: Union[pd.Timestamp, str] = None,
        filters: List = None,
        session: Session = None,
        order=None,
        limit: int = None,
        index: str = 'timestamp',
        index_is_time: bool = True,
        time_field: str = 'timestamp'):
    return get_data(data_schema=CashFlowStatement, entity_ids=entity_ids, entity_id=entity_id, codes=codes, level=level,
                    provider=provider,
                    columns=columns, return_type=return_type, start_timestamp=start_timestamp,
                    end_timestamp=end_timestamp, filters=filters, session=session, order=order, limit=limit,
                    index=index, index_is_time=index_is_time, time_field=time_field)


from zvt.domain import BigDealTrading

def get_big_deal_trading(
        entity_ids: List[str] = None,
        entity_id: str = None,
        codes: List[str] = None,
        level: Union[IntervalLevel, str] = None,
        provider: str = 'eastmoney',
        columns: List = None,
        return_type: str = 'df',
        start_timestamp: Union[pd.Timestamp, str] = None,
        end_timestamp: Union[pd.Timestamp, str] = None,
        filters: List = None,
        session: Session = None,
        order=None,
        limit: int = None,
        index: str = 'timestamp',
        index_is_time: bool = True,
        time_field: str = 'timestamp'):
    return get_data(data_schema=BigDealTrading, entity_ids=entity_ids, entity_id=entity_id, codes=codes, level=level,
                    provider=provider,
                    columns=columns, return_type=return_type, start_timestamp=start_timestamp,
                    end_timestamp=end_timestamp, filters=filters, session=session, order=order, limit=limit,
                    index=index, index_is_time=index_is_time, time_field=time_field)


from zvt.domain import IncomeStatement

def get_income_statement(
        entity_ids: List[str] = None,
        entity_id: str = None,
        codes: List[str] = None,
        level: Union[IntervalLevel, str] = None,
        provider: str = 'eastmoney',
        columns: List = None,
        return_type: str = 'df',
        start_timestamp: Union[pd.Timestamp, str] = None,
        end_timestamp: Union[pd.Timestamp, str] = None,
        filters: List = None,
        session: Session = None,
        order=None,
        limit: int = None,
        index: str = 'timestamp',
        index_is_time: bool = True,
        time_field: str = 'timestamp'):
    return get_data(data_schema=IncomeStatement, entity_ids=entity_ids, entity_id=entity_id, codes=codes, level=level,
                    provider=provider,
                    columns=columns, return_type=return_type, start_timestamp=start_timestamp,
                    end_timestamp=end_timestamp, filters=filters, session=session, order=order, limit=limit,
                    index=index, index_is_time=index_is_time, time_field=time_field)


from zvt.domain import TopTenTradableHolder

def get_top_ten_tradable_holder(
        entity_ids: List[str] = None,
        entity_id: str = None,
        codes: List[str] = None,
        level: Union[IntervalLevel, str] = None,
        provider: str = 'eastmoney',
        columns: List = None,
        return_type: str = 'df',
        start_timestamp: Union[pd.Timestamp, str] = None,
        end_timestamp: Union[pd.Timestamp, str] = None,
        filters: List = None,
        session: Session = None,
        order=None,
        limit: int = None,
        index: str = 'timestamp',
        index_is_time: bool = True,
        time_field: str = 'timestamp'):
    return get_data(data_schema=TopTenTradableHolder, entity_ids=entity_ids, entity_id=entity_id, codes=codes, level=level,
                    provider=provider,
                    columns=columns, return_type=return_type, start_timestamp=start_timestamp,
                    end_timestamp=end_timestamp, filters=filters, session=session, order=order, limit=limit,
                    index=index, index_is_time=index_is_time, time_field=time_field)


from zvt.domain import TopTenHolder

def get_top_ten_holder(
        entity_ids: List[str] = None,
        entity_id: str = None,
        codes: List[str] = None,
        level: Union[IntervalLevel, str] = None,
        provider: str = 'eastmoney',
        columns: List = None,
        return_type: str = 'df',
        start_timestamp: Union[pd.Timestamp, str] = None,
        end_timestamp: Union[pd.Timestamp, str] = None,
        filters: List = None,
        session: Session = None,
        order=None,
        limit: int = None,
        index: str = 'timestamp',
        index_is_time: bool = True,
        time_field: str = 'timestamp'):
    return get_data(data_schema=TopTenHolder, entity_ids=entity_ids, entity_id=entity_id, codes=codes, level=level,
                    provider=provider,
                    columns=columns, return_type=return_type, start_timestamp=start_timestamp,
                    end_timestamp=end_timestamp, filters=filters, session=session, order=order, limit=limit,
                    index=index, index_is_time=index_is_time, time_field=time_field)


from zvt.domain import StockMoneyFlow

def get_stock_money_flow(
        entity_ids: List[str] = None,
        entity_id: str = None,
        codes: List[str] = None,
        level: Union[IntervalLevel, str] = None,
        provider: str = 'sina',
        columns: List = None,
        return_type: str = 'df',
        start_timestamp: Union[pd.Timestamp, str] = None,
        end_timestamp: Union[pd.Timestamp, str] = None,
        filters: List = None,
        session: Session = None,
        order=None,
        limit: int = None,
        index: str = 'timestamp',
        index_is_time: bool = True,
        time_field: str = 'timestamp'):
    return get_data(data_schema=StockMoneyFlow, entity_ids=entity_ids, entity_id=entity_id, codes=codes, level=level,
                    provider=provider,
                    columns=columns, return_type=return_type, start_timestamp=start_timestamp,
                    end_timestamp=end_timestamp, filters=filters, session=session, order=order, limit=limit,
                    index=index, index_is_time=index_is_time, time_field=time_field)


from zvt.domain import MarginTrading

def get_margin_trading(
        entity_ids: List[str] = None,
        entity_id: str = None,
        codes: List[str] = None,
        level: Union[IntervalLevel, str] = None,
        provider: str = 'eastmoney',
        columns: List = None,
        return_type: str = 'df',
        start_timestamp: Union[pd.Timestamp, str] = None,
        end_timestamp: Union[pd.Timestamp, str] = None,
        filters: List = None,
        session: Session = None,
        order=None,
        limit: int = None,
        index: str = 'timestamp',
        index_is_time: bool = True,
        time_field: str = 'timestamp'):
    return get_data(data_schema=MarginTrading, entity_ids=entity_ids, entity_id=entity_id, codes=codes, level=level,
                    provider=provider,
                    columns=columns, return_type=return_type, start_timestamp=start_timestamp,
                    end_timestamp=end_timestamp, filters=filters, session=session, order=order, limit=limit,
                    index=index, index_is_time=index_is_time, time_field=time_field)


from zvt.domain import StockSummary

def get_stock_summary(
        entity_ids: List[str] = None,
        entity_id: str = None,
        codes: List[str] = None,
        level: Union[IntervalLevel, str] = None,
        provider: str = 'exchange',
        columns: List = None,
        return_type: str = 'df',
        start_timestamp: Union[pd.Timestamp, str] = None,
        end_timestamp: Union[pd.Timestamp, str] = None,
        filters: List = None,
        session: Session = None,
        order=None,
        limit: int = None,
        index: str = 'timestamp',
        index_is_time: bool = True,
        time_field: str = 'timestamp'):
    return get_data(data_schema=StockSummary, entity_ids=entity_ids, entity_id=entity_id, codes=codes, level=level,
                    provider=provider,
                    columns=columns, return_type=return_type, start_timestamp=start_timestamp,
                    end_timestamp=end_timestamp, filters=filters, session=session, order=order, limit=limit,
                    index=index, index_is_time=index_is_time, time_field=time_field)


from zvt.domain import FinanceFactor

def get_finance_factors(
        entity_ids: List[str] = None,
        entity_id: str = None,
        codes: List[str] = None,
        level: Union[IntervalLevel, str] = None,
        provider: str = 'eastmoney',
        columns: List = None,
        return_type: str = 'df',
        start_timestamp: Union[pd.Timestamp, str] = None,
        end_timestamp: Union[pd.Timestamp, str] = None,
        filters: List = None,
        session: Session = None,
        order=None,
        limit: int = None,
        index: str = 'timestamp',
        index_is_time: bool = True,
        time_field: str = 'timestamp'):
    return get_data(data_schema=FinanceFactor, entity_ids=entity_ids, entity_id=entity_id, codes=codes, level=level,
                    provider=provider,
                    columns=columns, return_type=return_type, start_timestamp=start_timestamp,
                    end_timestamp=end_timestamp, filters=filters, session=session, order=order, limit=limit,
                    index=index, index_is_time=index_is_time, time_field=time_field)


from zvt.domain import SpoDetail

def get_spo_detail(
        entity_ids: List[str] = None,
        entity_id: str = None,
        codes: List[str] = None,
        level: Union[IntervalLevel, str] = None,
        provider: str = 'eastmoney',
        columns: List = None,
        return_type: str = 'df',
        start_timestamp: Union[pd.Timestamp, str] = None,
        end_timestamp: Union[pd.Timestamp, str] = None,
        filters: List = None,
        session: Session = None,
        order=None,
        limit: int = None,
        index: str = 'timestamp',
        index_is_time: bool = True,
        time_field: str = 'timestamp'):
    return get_data(data_schema=SpoDetail, entity_ids=entity_ids, entity_id=entity_id, codes=codes, level=level,
                    provider=provider,
                    columns=columns, return_type=return_type, start_timestamp=start_timestamp,
                    end_timestamp=end_timestamp, filters=filters, session=session, order=order, limit=limit,
                    index=index, index_is_time=index_is_time, time_field=time_field)


from zvt.domain import ManagerTrading

def get_manager_trading(
        entity_ids: List[str] = None,
        entity_id: str = None,
        codes: List[str] = None,
        level: Union[IntervalLevel, str] = None,
        provider: str = 'eastmoney',
        columns: List = None,
        return_type: str = 'df',
        start_timestamp: Union[pd.Timestamp, str] = None,
        end_timestamp: Union[pd.Timestamp, str] = None,
        filters: List = None,
        session: Session = None,
        order=None,
        limit: int = None,
        index: str = 'timestamp',
        index_is_time: bool = True,
        time_field: str = 'timestamp'):
    return get_data(data_schema=ManagerTrading, entity_ids=entity_ids, entity_id=entity_id, codes=codes, level=level,
                    provider=provider,
                    columns=columns, return_type=return_type, start_timestamp=start_timestamp,
                    end_timestamp=end_timestamp, filters=filters, session=session, order=order, limit=limit,
                    index=index, index_is_time=index_is_time, time_field=time_field)


from zvt.domain import DividendDetail

def get_dividend_detail(
        entity_ids: List[str] = None,
        entity_id: str = None,
        codes: List[str] = None,
        level: Union[IntervalLevel, str] = None,
        provider: str = 'eastmoney',
        columns: List = None,
        return_type: str = 'df',
        start_timestamp: Union[pd.Timestamp, str] = None,
        end_timestamp: Union[pd.Timestamp, str] = None,
        filters: List = None,
        session: Session = None,
        order=None,
        limit: int = None,
        index: str = 'timestamp',
        index_is_time: bool = True,
        time_field: str = 'timestamp'):
    return get_data(data_schema=DividendDetail, entity_ids=entity_ids, entity_id=entity_id, codes=codes, level=level,
                    provider=provider,
                    columns=columns, return_type=return_type, start_timestamp=start_timestamp,
                    end_timestamp=end_timestamp, filters=filters, session=session, order=order, limit=limit,
                    index=index, index_is_time=index_is_time, time_field=time_field)


from zvt.domain import Stock

def get_stocks(
        entity_ids: List[str] = None,
        entity_id: str = None,
        codes: List[str] = None,
        level: Union[IntervalLevel, str] = None,
        provider: str = 'eastmoney',
        columns: List = None,
        return_type: str = 'df',
        start_timestamp: Union[pd.Timestamp, str] = None,
        end_timestamp: Union[pd.Timestamp, str] = None,
        filters: List = None,
        session: Session = None,
        order=None,
        limit: int = None,
        index: str = 'timestamp',
        index_is_time: bool = True,
        time_field: str = 'timestamp'):
    return get_data(data_schema=Stock, entity_ids=entity_ids, entity_id=entity_id, codes=codes, level=level,
                    provider=provider,
                    columns=columns, return_type=return_type, start_timestamp=start_timestamp,
                    end_timestamp=end_timestamp, filters=filters, session=session, order=order, limit=limit,
                    index=index, index_is_time=index_is_time, time_field=time_field)


from zvt.domain import InstitutionalInvestorHolder

def get_institutional_investor_holder(
        entity_ids: List[str] = None,
        entity_id: str = None,
        codes: List[str] = None,
        level: Union[IntervalLevel, str] = None,
        provider: str = 'eastmoney',
        columns: List = None,
        return_type: str = 'df',
        start_timestamp: Union[pd.Timestamp, str] = None,
        end_timestamp: Union[pd.Timestamp, str] = None,
        filters: List = None,
        session: Session = None,
        order=None,
        limit: int = None,
        index: str = 'timestamp',
        index_is_time: bool = True,
        time_field: str = 'timestamp'):
    return get_data(data_schema=InstitutionalInvestorHolder, entity_ids=entity_ids, entity_id=entity_id, codes=codes, level=level,
                    provider=provider,
                    columns=columns, return_type=return_type, start_timestamp=start_timestamp,
                    end_timestamp=end_timestamp, filters=filters, session=session, order=order, limit=limit,
                    index=index, index_is_time=index_is_time, time_field=time_field)


from zvt.domain import DividendFinancing

def get_dividend_financing(
        entity_ids: List[str] = None,
        entity_id: str = None,
        codes: List[str] = None,
        level: Union[IntervalLevel, str] = None,
        provider: str = 'eastmoney',
        columns: List = None,
        return_type: str = 'df',
        start_timestamp: Union[pd.Timestamp, str] = None,
        end_timestamp: Union[pd.Timestamp, str] = None,
        filters: List = None,
        session: Session = None,
        order=None,
        limit: int = None,
        index: str = 'timestamp',
        index_is_time: bool = True,
        time_field: str = 'timestamp'):
    return get_data(data_schema=DividendFinancing, entity_ids=entity_ids, entity_id=entity_id, codes=codes, level=level,
                    provider=provider,
                    columns=columns, return_type=return_type, start_timestamp=start_timestamp,
                    end_timestamp=end_timestamp, filters=filters, session=session, order=order, limit=limit,
                    index=index, index_is_time=index_is_time, time_field=time_field)
