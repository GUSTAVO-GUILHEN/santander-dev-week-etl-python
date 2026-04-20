import pandas as pd
import google.generativeai as genai
import os

# CONFIGURAÇÃO DA IA
genai.configure(api_key="SUA_CHAVE_AQUI")
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_ai_news(user_name, balance):
    """Função isolada para a etapa de TRANSFORMAÇÃO"""
    prompt = f"Você é um gerente do Santander. Crie uma frase curta (máximo 100 caracteres) para o cliente {user_name}, que tem saldo de R${balance}, incentivando-o a investir no CDB."
    
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return "Invista hoje e garanta seu futuro!" # Fallback caso a API falhe

# --- FLUXO ETL ---

# 1. EXTRACT
df = pd.read_csv('SDW2023.csv')

# 2. TRANSFORM
print("Gerando mensagens com IA...")
# O .apply do Pandas é muito mais performático que um loop 'for' manual
df['news'] = df.apply(lambda row: generate_ai_news(row['Nome'], row['Saldo']), axis=1)

# 3. LOAD
df.to_csv('SDW2023_FINAL.csv', index=False)
print("Sucesso! Arquivo gerado.")