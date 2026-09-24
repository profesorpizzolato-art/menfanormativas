```python
import streamlit as st

from paginas import inicio
from paginas import biblioteca
from paginas import favoritos
from paginas import perfil
from paginas import administracion


# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================

st.set_page_config(
    page_title="MENFANormativas",
    page_icon="📚",
    layout="wide"
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("MENFANormativas")

opcion = st.sidebar.radio(
    "Menú",
    [
        "Inicio",
        "Biblioteca",
        "Favoritos",
        "Perfil",
        "Administración"
    ]
)


# ============================================================
# NAVEGACIÓN
# ============================================================

if opcion == "Inicio":
    inicio.mostrar()

elif opcion == "Biblioteca":
    biblioteca.mostrar()

elif opcion == "Favoritos":
    favoritos.mostrar()

elif opcion == "Perfil":
    perfil.mostrar()

elif opcion == "Administración":
    administracion.mostrar()


# ============================================================
# PIE DEL SIDEBAR
# ============================================================

st.sidebar.markdown("---")

st.sidebar.caption("MENFANormativas · Versión MVP 1.0")
```

### ⚠️ Pero hay algo importante

Este `app.py` **solamente va a funcionar si tu estructura de carpetas es compatible**. Por ejemplo:

```text
MENFANormativas/
│
├── app.py
│
└── paginas/
    ├── __init__.py
    ├── inicio.py
    ├── biblioteca.py
    ├── favoritos.py
    ├── perfil.py
    └── administracion.py
```

Y cada módulo debería tener una función `mostrar()`.

Por ejemplo:

```python
# paginas/inicio.py

import streamlit as st


def mostrar():
    st.title("MENFANormativas")
    st.write("Bienvenido al sistema de normativas de MENFA.")
```

Y:

```python
# paginas/biblioteca.py

import streamlit as st


def mostrar():
    st.title("Biblioteca")
    st.write("Aquí estarán las normas y documentos.")
```

### Hay además una decisión que te recomiendo para MENFANormativas

Para el MVP está bien este sistema de navegación manual. **No lo cambiaría todavía** si ya estás construyendo las distintas secciones.

Más adelante podemos pasar a la navegación multipágina nativa de Streamlit (`st.Page` + `st.navigation`), que actualmente está soportada oficialmente.

Pero para tu proyecto actual yo mantendría:

```text
app.py
│
├── paginas/
│   ├── inicio.py
│   ├── biblioteca.py
│   ├── favoritos.py
│   ├── perfil.py
│   └── administracion.py
│
├── datos/
│
├── normas/
│
├── componentes/
│
└── assets/
```

Eso nos deja una base mucho más limpia para después incorporar **ISO + API + ASME + IRAM + NFPA**, buscador, fichas de normas, favoritos, usuarios y eventualmente acceso comercial.

**Si me pasás ahora los archivos de `paginas/` (o el código completo del proyecto), puedo revisar el conjunto**, porque el siguiente punto crítico es verificar que cada `mostrar()` exista y que no haya imports circulares o errores de estado.
