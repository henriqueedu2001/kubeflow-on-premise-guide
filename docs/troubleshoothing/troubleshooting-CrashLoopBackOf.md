# CrashLoopBackOf
Erro indica que o pod não foi iniciado corretamente. 

## Motivos
- Pod talvez dependa de outro para iniciar corretamente.
- Falha dentro do pod. 

## Recomendações
Como esse erro depende de pod para pod recomendamos que tente descobrir onde está a falha de o seguinte 
comando `kubectl describe pod <nome-do-pod>` ou `kubectl logs <nome-do-pod> -n <namespace>`
