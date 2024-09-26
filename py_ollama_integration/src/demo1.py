import ollama

response = ollama.chat(model='llama3', messages=[{
    'role' : 'user',
    'content' : 'Give me workout plan for a week'
}])

print(response)