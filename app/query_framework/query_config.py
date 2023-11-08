class QueryConfig:
    DEFAULT_PARAMS_TYPES = {
        "country": "STRING",
        "region": "STRING",
        "segment": "STRING",
        "product": "STRING",
        "top_category": "STRING",
        "only_promo": "STRING",
        "top_subcategory": "STRING",
        "regular_buyer": "STRING",
        "extended_group": "BOOL",
        "exclude_high_risk_customers": "BOOL",
        "exclude_low_risk_customers": "BOOL",
    }
    BASE_SQL = "SELECT * FROM `data-to-insights.ecommerce.all_sessions_raw` \
        \nWHERE"