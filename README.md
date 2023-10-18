# 项目环境

- langchain
- streamlit
- python-dotenv
- qianfan

# 1.构建环境

```python
python -m venv .venv
```
# 2.安装项目环境

```python
pip install langchain streamlit python-dotenv qianfan

```

# 3.加载api key

```
QIANFAN_AK="yout_ak"
QIANFAN_SK="yout_sk"
```

# 4. 编写demo程序

```python
from langchain.llms import QianfanLLMEndpoint
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name():
    llm = QianfanLLMEndpoint(temperature=0.6)
    names = llm.predict('帮我给我的宠物猫取一个名字,我只需要结果')
    return names

if __name__ == '__main__':
    print(generate_pet_name())
```

如果以上代码运行正常,则说明你的环境没有问题,可以进行下一步操作了

# 5. 使用prompt 提示词模板和chians来管理

```python
from langchain.llms import QianfanLLMEndpoint
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

prompt_template_name = PromptTemplate(
    input_variables=['animal_type'],
    template="帮我给我的宠物{animal_type}取5个名字,我只需要结果"

)

def generate_pet_name(animal_type):
    llm = QianfanLLMEndpoint(temperature=0.6)
    name_chains = LLMChain(llm=llm,prompt=prompt_template_name)
    resp = name_chains.run(animal_type)
    return resp

if __name__ == '__main__':
    print(generate_pet_name("猫"))
```

到这里你已经完全跟上了节奏,那么接下来让我们构建一个Web界面来使用这个应用!

# 6. 使用streamlit 构建Web界面

```python
import qianfan_helper as qf

import streamlit as st
import time


st.title('智能宠物取名系统')

animal_type = st.sidebar.selectbox('你的宠物是?',['猫','狗','猪','松鼠','鸭鸭'])

color = st.sidebar.text_input('宠物的颜色是?',max_chars=15)

clicked = st.sidebar.button('试试手气')

if clicked:
    st.markdown(qf.generate_pet_name(animal_type,color))
    time.sleep(2)

```

# 7. 启动项目

```python

streamlit run filename

streamlit run streamlit_app.py
```