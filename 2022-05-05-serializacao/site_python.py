import json


cadeia_caracteres = '{"en": "English","es": "Spanish","fr": "French","ja": "Japanese","ko": "Korean", "pt-br": "Brazilian Portuguese", "zh-cn": "Simplified Chinese", "zh-tw": "Traditional Chinese"}'

dicionario = json.loads(cadeia_caracteres)

cadeia_caracteres = ''

cadeia_caracteres = json.dumps(dicionario)


print(dicionario['en'])

print(dicionario['pt-br'])