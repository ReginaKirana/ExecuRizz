def reachTop(N, P, G):
    for strength in G:
        if P >= strength:
            P += strength
        else:
            return "NO"  # Pahlawan terhenti
    return "YES"  # Pahlawan mencapai puncak
data = input().split()
N, P = int(data[0]), int(data[1])
G = list(map(int, input().split()))
print(reachTop(N, P, G))