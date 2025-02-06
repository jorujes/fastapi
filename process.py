import os
import sys
import aiohttp
import asyncio
import concurrent.futures
import nest_asyncio
import re
import random
import requests
import time
import threading
from typing import Any, List, Optional, Dict, Tuple
from datetime import datetime

# Importações de bibliotecas externas
import openai
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT, WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from docx.enum.style import WD_STYLE_TYPE

# Configurar a API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("A chave da OpenAI não foi configurada corretamente no Railway!")

def gerar_indice(discipline, theme, text_type, total_pages):
    """
    Gera um índice para um documento acadêmico baseado nos parâmetros fornecidos.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": f"Você é um especialista acadêmico. Elabore um índice com que respeite a seguinte regra de número de itens: dois terços de {total_pages}. Esse número deve ser o TOTAL, dividido entre entre tópicos e subtópicos, de uma '{text_type}' sobre o tema '{theme}' no contexto do curso de '{discipline}'. Use o formato 1. para numerar tópicos principais (2., 3., 4., assim por diante) e 1.1 para numerar subtópicos (1.2, 1.3, 1.4, 2.1, 2.2, 2.3 assim por diante). Certifique-se de que o índice reflita uma progressão lógica e coerente das ideias e evite redundâncias. Não acrescente mais nada (asteriscos, comentários, etc) ao índice além do pedido"}
            ]
        )

        resultado = response['choices'][0]['message']['content']
        return [{"title": linha.strip()} for linha in resultado.strip().split('\n') if linha.strip()]
    
    except Exception as e:
        return {"erro": f"Erro ao chamar OpenAI: {str(e)}"}

def executar_processo_completo(discipline, theme, text_type, total_pages):
    """
    Executa o processo completo: gera o índice e retorna os resultados.
    """
    indice = gerar_indice(discipline, theme, text_type, total_pages)
    return indice
