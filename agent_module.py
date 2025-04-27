
from groq import Groq
import os
from langchain.schema import HumanMessage, SystemMessage
from langchain_groq import ChatGroq

# Inicializar cliente Groq
client = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name=os.getenv("GROQ_MODEL", "llama3-70b-8192")
)

class ModularAgent:
    def __init__(self, name):
        self.name = name
        self.messages = []
        self.token_counter = {"input": 0, "output": 0, "total": 0}

    def run(self, system_prompt, user_prompt, max_tokens=1500):
        self.messages.append(SystemMessage(content=system_prompt))
        self.messages.append(HumanMessage(content=user_prompt))
        
        response = client(messages=self.messages, max_tokens=max_tokens)
        
        answer = response.content
        
        # Guardar respuesta
        self.messages.append(HumanMessage(content=answer))
        
        usage = response.response_metadata.get("usage", {})
        if usage:
            self.token_counter["input"] += usage.get("prompt_tokens", 0)
            self.token_counter["output"] += usage.get("completion_tokens", 0)
            self.token_counter["total"] += usage.get("total_tokens", 0)
        else:
            # Estimar tokens
            estimated_input_tokens = sum(len(m.content) for m in self.messages if isinstance(m, HumanMessage)) // 4
            estimated_output_tokens = len(answer) // 4
            self.token_counter["input"] += estimated_input_tokens
            self.token_counter["output"] += estimated_output_tokens
            self.token_counter["total"] += estimated_input_tokens + estimated_output_tokens
        
        return answer

def query_razonamiento(question):
    agents = {
        "explorer": ModularAgent("Explorador"),
        "strategist": ModularAgent("Estratega"),
        "solver": ModularAgent("Solucionador"),
        "researcher": ModularAgent("Investigador Web"),
        "architect": ModularAgent("Arquitecto"),
        "reviewer": ModularAgent("Revisor")
    }

    # Fases
    exploration = agents["explorer"].run(
        "Tu rol es explorar el contexto general de un problema complejo.",
        f"Explora ampliamente sobre: {question}"
    )

    strategy = agents["strategist"].run(
        "Tu rol es proponer estrategias basadas en la exploración previa.",
        f"Basado en la exploración: {exploration}, desarrolla estrategias."
    )

    solution = agents["solver"].run(
        "Tu rol es encontrar soluciones prácticas al problema.",
        f"Basado en las estrategias: {strategy}, propone soluciones para: {question}"
    )

    research = agents["researcher"].run(
        "Tu rol es citar artículos, autores o papers relevantes sobre el tema.",
        f"Cita referencias relevantes sobre: {question}"
    )

    final_draft = agents["architect"].run(
        "Tu rol es sintetizar toda la información en una respuesta integral.",
        f"Usa:\n- Exploración: {exploration}\n- Estrategia: {strategy}\n- Soluciones: {solution}\n- Referencias: {research}\n\nResponde a: {question}"
    )

    final_answer = agents["reviewer"].run(
        "Tu rol es revisar y mejorar el texto para que sea claro y profesional. Opcionalmente sugiere mejoras.",
        f"Texto a revisar:\n\n{final_draft}"
    )

    input_tokens = sum(agent.token_counter["input"] for agent in agents.values())
    output_tokens = sum(agent.token_counter["output"] for agent in agents.values())
    total_tokens = sum(agent.token_counter["total"] for agent in agents.values())
    reasoning_tokens = sum(agent.token_counter["total"] for k, agent in agents.items() if k != "reviewer")

    return {
        "answer": final_answer,
        "tokens": {
            "input": input_tokens,
            "output": output_tokens,
            "reasoning": reasoning_tokens,
            "total": total_tokens
        },
        "intermediate_steps": {
            "Exploración": exploration,
            "Estrategia": strategy,
            "Soluciones": solution,
            "Investigación Web": research,
            "Borrador Final": final_draft
        },
        "agents": agents
    }
