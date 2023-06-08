-- Query to request data on the number of homicides in Argentina
SELECT anio,cantidad_hechos, LOWER(provincia_nombre) AS provincia_nombre,codigo_delito_snic_id
FROM df
WHERE codigo_delito_snic_id IN (1)