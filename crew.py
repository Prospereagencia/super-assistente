import yaml
import os
from pathlib import Path
from crewai import Agent, Task, Crew, Process

class MeuAssistenteCrew:
    def __init__(self):
        self.config_path = Path(__file__).parent / "config"
        self.agents_config = self._load_config("agents.yaml")
        self.tasks_config = self._load_config("tasks.yaml")
        
    def _load_config(self, filename):
        """Carrega configurações YAML"""
        config_file = self.config_path / filename
        with open(config_file, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
    
    def _create_agents(self):
        """Cria os agentes baseado na configuração"""
        agents = {}
        
        for agent_name, config in self.agents_config.items():
            agents[agent_name] = Agent(
                role=config['role'],
                goal=config['goal'],
                backstory=config['backstory'],
                verbose=config.get('verbose', True),
                allow_delegation=config.get('allow_delegation', False)
            )
        
        return agents
    
    def _create_tasks(self, agents, task_names=None):
        """Cria as tarefas baseado na configuração"""
        if task_names is None:
            task_names = ['apresentacao']  # tarefa padrão
            
        tasks = []
        
        for task_name in task_names:
            if task_name in self.tasks_config:
                config = self.tasks_config[task_name]
                task = Task(
                    description=config['description'],
                    expected_output=config['expected_output'],
                    agent=agents['assistente_pessoal']  # agente padrão
                )
                tasks.append(task)
        
        return tasks
    
    def create_crew(self, task_names=None):
        """Cria e retorna o crew completo"""
        agents = self._create_agents()
        tasks = self._create_tasks(agents, task_names)
        
        crew = Crew(
            agents=list(agents.values()),
            tasks=tasks,
            verbose=2,
            process=Process.sequential
        )
        
        return crew
    
    def run_apresentacao(self):
        """Executa a tarefa de apresentação"""
        crew = self.create_crew(['apresentacao'])
        return crew.kickoff()
    
    def run_organizacao_tarefas(self, tarefas_usuario=None):
        """Executa a tarefa de organização"""
        crew = self.create_crew(['organizacao_tarefas'])
        return crew.kickoff()
    
    def run_pesquisa(self, topico=None):
        """Executa a tarefa de pesquisa"""
        crew = self.create_crew(['pesquisa_informacoes'])
        return crew.kickoff()