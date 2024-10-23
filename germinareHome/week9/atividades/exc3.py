def filtar_historico_clientes(listaClientes, idadeMin, idadeMax, locDesejada, valorMinimoDeCompras):
    clientesFiltrados = set()

    for cliente in listaClientes:
        if(idadeMin<= cliente[1] <= idadeMax):
            if(cliente[2] == locDesejada):
                if(cliente[3] >= valorMinimoDeCompras):
                    clientesFiltrados.add(cliente)
        
    return clientesFiltrados