# список сервера и что в нем находится
def get_server(client):
    print(f"\n\nServer")
    parameters_Server = [
        client.get_endpoints()[0].Server.ProductUri,
        client.get_endpoints()[0].Server.ApplicationUri,
        client.get_endpoints()[0].Server.ApplicationName,
        client.get_endpoints()[0].Server.ApplicationType,
        client.get_endpoints()[0].Server.GatewayServerUri,
        client.get_endpoints()[0].Server.DiscoveryProfileUri,
        client.get_endpoints()[0].Server.DiscoveryUrls
        ]

    keys = [
        "ProductUri",
        "ApplicationUri",
        "ApplicationName",
        "ApplicationType",
        "GatewayServerUri",
        "DiscoveryProfileUri",
        "DiscoveryUrls",
        ]

    for i in range(len(parameters_Server)):
        print(f"{keys[i]}: \t{parameters_Server[i]}")
    
    
    

# список токенов и что в них находится
def get_user_identity_tokens(client):
    print(f"\n\nUserIdentityTokens")
    parameters_UserIdentityTokens = [
        client.get_endpoints()[0].UserIdentityTokens[1].PolicyId,
        client.get_endpoints()[0].UserIdentityTokens[0].PolicyId,
        client.get_endpoints()[0].UserIdentityTokens[1].TokenType,
        client.get_endpoints()[0].UserIdentityTokens[0].TokenType,
        client.get_endpoints()[0].UserIdentityTokens[1].IssuedTokenType,
        client.get_endpoints()[0].UserIdentityTokens[0].IssuedTokenType,
        client.get_endpoints()[0].UserIdentityTokens[1].IssuerEndpointUrl,
        client.get_endpoints()[0].UserIdentityTokens[0].IssuerEndpointUrl,
        client.get_endpoints()[0].UserIdentityTokens[1].SecurityPolicyUri,
        client.get_endpoints()[0].UserIdentityTokens[0].SecurityPolicyUri,
    ]
    keys = [
        "PolicyId",
        "TokenType",
        "IssuedTokenType",
        "IssuerEndpointUrl",
        "SecurityPolicyUri",
        ]


    even, odd, i = 0, 1, 0

    while odd<=len(parameters_UserIdentityTokens):
        print(keys[i], end=': ')
        print(f"\t{parameters_UserIdentityTokens[even]} - {parameters_UserIdentityTokens[odd]}")
        i+=1
        odd+=2
        even+=2    
    

