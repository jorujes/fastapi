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

# Configuração global da chave de API (pega do Railway)
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("A chave da OpenAI não foi configurada corretamente no Railway!")