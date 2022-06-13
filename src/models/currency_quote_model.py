from dataclasses import dataclass


@dataclass
class CurrencyQuoteModel:
    code: str
    codein: str
    name: str
    high: str
    low: str
    varBid: str
    pctChange: str
    bid: str
    ask: str
    timestamp: str
    create_date: str

    @staticmethod
    def parseToObject(json: dict[str, str]):
        return CurrencyQuoteModel(
            code=json['code'],
            codein=json['codein'],
            name=json['name'],
            high=json['high'],
            low=json['low'],
            varBid=json['varBid'],
            pctChange=json['pctChange'],
            bid=json['bid'],
            ask=json['ask'],
            timestamp=json['timestamp'],
            create_date=json['create_date']
        )
