def get_geometry_type(self, table_name, geo_col):
    cursor = self.connection.cursor()
    try:
        cursor.execute('DESCRIBE %s' %
                        self.connection.ops.quote_name(table_name))
        for column, typ, null, key, default, extra in cursor.fetchall():
            if column == geo_col:
                field_type = "OGRGeomType"(typ).django      # 'OGRGeomType' 관련 데이터 없으므로 문자열 처리 
                field_params = {}
                # break 전에 닫기
                cursor.close()
                break
    except:
        # 예외가 발생했을 때 닫기
        cursor.close()
    # 정상적으로 끝났을 때 닫기      / 위에서 if 조건문에 안 들어갔을 수 있으므로 닫아야 한다.
    cursor.close()