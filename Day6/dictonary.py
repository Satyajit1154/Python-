info={
    "name":"satyajit",
    "cgpa":8.4,
    "subjects":["math","science"],
}
print(info)
print(info.items())
print(info.values())
print(info.keys())

print(info.get("cgpa"))
print("Code Ended")

info.update({
    "city":"delhi"
})

print(info)