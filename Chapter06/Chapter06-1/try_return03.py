def get_geometry_type(self, table_name, geo_col):
    cursor = self.connection.cursor()
    try:
        cursor.execute('DESCRIBE %s' %
                        self.connection.ops.quote_name(table_name))
        for column, typ, null, key, default, extra in cursor.fetchall():
            if column == geo_col:
                field_type = "OGRGeomType"(typ).django      # 'OGRGeomType' 관련 데이터 없으므로 문자열 처리 
                field_params = {}
                break
    finally:
        cursor.close()      # finally 사용
    