# Cybersecurity Python Labs

## Visão geral

Este repositório reúne pequenos labs educacionais em Python para estudo de fundamentos de cibersegurança. O conteúdo deve ser usado exclusivamente em ambientes locais, redes isoladas, máquinas próprias ou cenários com autorização explícita.

Os scripts são exercícios didáticos. Não são ferramentas aprovadas para operações ofensivas reais.

## Escopo ético

Antes de executar qualquer lab:

- Tenha autorização formal para o ambiente testado.
- Prefira `localhost`, `127.0.0.1` e redes de laboratório.
- Use endereços reservados para documentação, como `192.0.2.1`.
- Não use credenciais, telefones, URLs, arquivos ou dados pessoais reais.
- Não publique saídas de varredura ou informações coletadas de terceiros.

## Labs disponíveis

| Diretório | Finalidade didática |
| --- | --- |
| `Gerador de Hash/` | Estudo de funções hash. |
| `Comparador de Hash/` | Comparação local de hashes. |
| `Gerador de Senhas/` | Geração local de senhas. |
| `Gerador de Wordlist/` | Permutações de texto para aprendizado. Não usar contra contas reais. |
| `PortScanner/` | Fundamentos de sockets e integração com Nmap em laboratório autorizado. |
| `CLI Incompletas/PING/` | Exemplos básicos de conectividade local. |
| `CLI Incompletas/SOCKET/` | Estudos de clientes e servidores socket locais. |
| `CLI Incompletas/Threads e IPs/` | Exercícios de threads e endereços IP reservados. |
| `Web Crawling/` | Parsing de páginas locais ou explicitamente autorizadas. |
| `Web Scraping/` | Estudo de HTML em URLs autorizadas. |
| `Ocultados de Arquivos/` | Esteganografia com mensagem fictícia em arquivo local. |
| `Verificador de IP Externo/` | Consulta de metadados do próprio IP externo. |
| `CheckList Telefônico/` | Estudo de metadados apenas com números fictícios ou autorizados. |
| `Ferramenta Grafica/` | Atalhos locais para recursos externos de estudo. |

## Instalação

Crie um ambiente virtual e instale as dependências:

```bash
python -m venv .venv
pip install -r requirements.txt
```

Ative o ambiente virtual conforme seu sistema operacional antes de executar um lab.

## Placeholders seguros

Use valores deste tipo em exemplos:

- Host local: `localhost`
- Loopback: `127.0.0.1`
- IP reservado para documentação: `192.0.2.1`
- URL reservada: `https://example.com/`
- Texto fictício: `LAB_PLACEHOLDER_MESSAGE`

## Limitações

- Alguns scripts são estudos iniciais ou incompletos.
- Scripts de rede podem gerar tráfego e devem ficar restritos ao laboratório.
- Serviços externos podem coletar metadados da requisição.
- O repositório não fornece instruções para uso contra alvos reais.

## Segurança

Consulte [SECURITY.md](../../SECURITY.md) e [SECURITY_NOTES.md](../../SECURITY_NOTES.md).
