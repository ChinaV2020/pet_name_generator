from langchain.llms import QianfanLLMEndpoint
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

prompt_template_name = PromptTemplate(
    input_variables=['animal_type','color'],
    template="帮我的{color}的宠物{animal_type}取5个名字,我只需要结果"

)

def generate_pet_name(animal_type,color):
    llm = QianfanLLMEndpoint(temperature=0.6)
    name_chains = LLMChain(llm=llm,prompt=prompt_template_name)
    resp = name_chains.run({'animal_type':animal_type,'color':color})
    return resp



if __name__ == "__main__":
    print(generate_pet_name('猫','白色'))