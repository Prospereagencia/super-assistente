#!/usr/bin/env python3
"""
Meu Assistente Pessoal - CrewAI
"""

import sys
from .crew import MeuAssistenteCrew

def main():
    """Função principal do assistente"""
    print("🤖 Iniciando Meu Assistente Pessoal...")
    print("=" * 60)
    
    try:
        # Criar instância do crew
        assistente = MeuAssistenteCrew()
        
        # Verificar argumentos da linha de comando
        if len(sys.argv) > 1:
            comando = sys.argv[1].lower()
            
            if comando == "apresentacao":
                resultado = assistente.run_apresentacao()
            elif comando == "organizar":
                resultado = assistente.run_organizacao_tarefas()
            elif comando == "pesquisar":
                resultado = assistente.run_pesquisa()
            else:
                print(f"Comando '{comando}' não reconhecido.")
                print("Comandos disponíveis: apresentacao, organizar, pesquisar")
                return
        else:
            # Executar apresentação por padrão
            resultado = assistente.run_apresentacao()
        
        # Exibir resultado
        print("\n" + "=" * 60)
        print("🎯 RESULTADO:")
        print("=" * 60)
        print(resultado)
        
    except Exception as e:
        print(f"❌ Erro ao executar o assistente: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()