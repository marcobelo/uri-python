SELECT pd.name, pv.name
FROM products AS pd, providers AS pv
WHERE pd.id_providers = pv.id AND pv.name = 'Ajax SA';
