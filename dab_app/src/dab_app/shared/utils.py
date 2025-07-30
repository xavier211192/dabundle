"""Shared utilities for all jobs"""


def get_config(env: str) -> dict:
    """Get configuration based on environment"""
    configs = {
        'dev': {
            'database': 'dev_db',
            'log_level': 'DEBUG',
            'batch_size': 100
        },
        'staging': {
            'database': 'staging_db', 
            'log_level': 'INFO',
            'batch_size': 500
        },
        'prod': {
            'database': 'prod_db',
            'log_level': 'WARN', 
            'batch_size': 1000
        }
    }
    
    return configs.get(env, configs['dev'])


def setup_logging(level: str = 'INFO'):
    """Setup logging configuration"""
    import logging
    
    logging.basicConfig(
        level=getattr(logging, level),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    return logging.getLogger(__name__)