import yaml
import pymysql
import logging
from typing import Union

logger = logging.getLogger(__name__)

class MySQLConn:
    def __init__(self, db_env: Union[int, str], autocommit: bool=True, dict_mode: bool=True) -> None:
        self.db_env = db_env
        self.autocommit = autocommit
        self.dict_mode = dict_mode

    def cursor(self,):
        db_info = yaml.load(open('dbconfig.yaml'), yaml.loader.SafeLoader)
        db = f"mysql_{self.db_env}"
        db_cfg = db_info[db]

        host=db_cfg['host']
        port=db_cfg['port']
        user=db_cfg['user']
        password=db_cfg['password']
        
        logger.info("=================================================")
        logger.info("our db_config:")
        logger.info(f"host: {host}")
        logger.info(f"port: {port}")
        logger.info(f"user: {user}")
        logger.info(f"password: {password}")
        logger.info(f"autocommit: {self.autocommit}")
        logger.info(f"dictionary mode: {self.dict_mode}")
        logger.info("=================================================")
        if self.dict_mode:
            self.connection = pymysql.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                autocommit=self.autocommit,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        else:
            self.connection = pymysql.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                autocommit=self.autocommit,
                charset='utf8mb4',
            )

        return self.connection.cursor()
        
    def close(self,):
        self.connection.close()