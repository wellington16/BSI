import wx


class GameFrame(wx.Frame):
    
    def __init__(self,  pparent, pid, ptitle,  psize):
            wx.Frame.__init__(self, pparent, pid,  ptitle, size=psize)
            painel = wx.Panel(self)
            menubar = wx.MenuBar()
            Jogo = wx.Menu()
            Ver = wx.Menu()
            Definicoes= wx.Menu()
            Jogo.Append(101, '&Novo', 'Inicia um novo jogo')
            Jogo.Append(102, '&Pausa', 'Mete o jogo em pausa')
            Jogo.Append(106, '&Activar Sons', 'Activa os sons',  wx.ITEM_CHECK)
            Jogo.AppendSeparator()
            Sair = wx.MenuItem(Jogo, 105, '&Sair\tCtrl+Q', 'Sai do jogo')
            Jogo.AppendItem(Sair)

            Ver.Append(103,'&Ecran Completo\tCtrl+E', 'Apresenta o modo de ecran completo')

            Definicoes.Append(104,'&Preferencias', 'Configurar o jogo') 

            menubar.Append(Jogo, 'Jogo')
            menubar.Append(Ver, '&Ver')
            menubar.Append(Definicoes, '&Definicoes')
            self.SetMenuBar(menubar)
            self.CreateStatusBar()

    # grelha de jogo
    for i in range(1, 11):
        wx.StaticText(painel, wx.ID_ANY, chr(i+64), size=(20, 30),  pos=(20+25*i, 20))
    for i in range(11, 21):
        wx.StaticText(painel, wx.ID_ANY, chr(i+54), size=(20, 30),  pos=(50+25*i, 20))
    for i in range(1,  11):
        for j in range(1,  11):
            wx.Button(painel, 10000+i*100+j,  "", size=(20, 30),  pos=(20+25*j, i*30+10))
    for j in range(11,  21):
        wx.Button(painel, 20000+i*100+j,  "", size=(20, 30),  pos=(50+25*j, i*30+10))
    for i in range(1, 11):
        wx.StaticText(painel, wx.ID_ANY, str(i), size=(20, 30), pos=(300, i*30+10))

    # botoes para posicionar barcos
    self.bt2hc1 = wx.Button(painel, 30010,  "", size=(20, 30),  pos=(50, 350))
    self.bt2hc2 = wx.Button(painel, 30020,  "", size=(20, 30),  pos=(70, 350))
    self.bt3hc1 = wx.Button(painel, 30030,  "", size=(20, 30),  pos=(50, 390))
    self.bt3hc2 = wx.Button(painel, 30040,  "", size=(20, 30),  pos=(70, 390))
    self.bt3hc3 = wx.Button(painel, 30050,  "", size=(20, 30),  pos=(90, 390))
    self.bt4hc1 = wx.Button(painel, 30060,  "", size=(20, 30),  pos=(50, 430))
    self.bt4hc2 = wx.Button(painel, 30070,  "", size=(20, 30),  pos=(70, 430))
    self.bt4hc3 = wx.Button(painel, 30080,  "", size=(20, 30),  pos=(90, 430))
    self.bt4hc3 = wx.Button(painel, 30090,  "", size=(20, 30),  pos=(110, 430))

    self.bt2vc1 = wx.Button(painel, 30010,  "", size=(20, 30),  pos=(200, 350))
    self.bt2vc2 = wx.Button(painel, 30020,  "", size=(20, 30),  pos=(200, 380))
    self.bt3vc1 = wx.Button(painel, 30010,  "", size=(20, 30),  pos=(230, 350))
    self.bt3vc2 = wx.Button(painel, 30020,  "", size=(20, 30),  pos=(230, 380))
    self.bt3vc3 = wx.Button(painel, 30020,  "", size=(20, 30),  pos=(230, 410))
    self.bt4vc1 = wx.Button(painel, 30010,  "", size=(20, 30),  pos=(260, 350))
    self.bt4vc2 = wx.Button(painel, 30020,  "", size=(20, 30),  pos=(260, 380))
    self.bt4vc3 = wx.Button(painel, 30020,  "", size=(20, 30),  pos=(260, 410))
    self.bt4vc4 = wx.Button(painel, 30020,  "", size=(20, 30),  pos=(260, 440))

    # porta-avioes
    self.btapp11 = wx.Button(painel, 30010,  "", size=(20, 30),  pos=(290, 350))
    self.btapp12 = wx.Button(painel, 30020,  "", size=(20, 30),  pos=(290, 380))
    self.btapp13 = wx.Button(painel, 30020,  "", size=(20, 30),  pos=(290, 410))
    self.btapp14 = wx.Button(painel, 30020,  "", size=(20, 30),  pos=(310, 380))
    self.btapp15 = wx.Button(painel, 30020,  "", size=(20, 30),  pos=(330, 380))

    self.btapp21 = wx.Button(painel, 30010,  "", size=(20, 30),  pos=(400, 350))
    self.btapp22 = wx.Button(painel, 30020,  "", size=(20, 30),  pos=(400, 380))
    self.btapp23 = wx.Button(painel, 30020,  "", size=(20, 30),  pos=(400, 410))
    self.btapp24 = wx.Button(painel, 30020,  "", size=(20, 30),  pos=(360, 380))
    self.btapp25 = wx.Button(painel, 30020,  "", size=(20, 30),  pos=(380, 380))

    self.btapp31 = wx.Button(painel, 30010,  "", size=(20, 30),  pos=(430, 350))
    self.btapp32 = wx.Button(painel, 30020,  "", size=(20, 30),  pos=(450, 350))
    self.btapp33 = wx.Button(painel, 30020,  "", size=(20, 30),  pos=(470, 350))
    self.btapp34 = wx.Button(painel, 30020,  "", size=(20, 30),  pos=(450, 380))
    self.btapp35 = wx.Button(painel, 30020,  "", size=(20, 30),  pos=(450, 410))

    self.btapp41 = wx.Button(painel, 30010,  "", size=(20, 30),  pos=(500, 410))
    self.btapp42 = wx.Button(painel, 30020,  "", size=(20, 30),  pos=(520, 410))
    self.btapp43 = wx.Button(painel, 30020,  "", size=(20, 30),  pos=(540, 410))
    self.btapp44 = wx.Button(painel, 30020,  "", size=(20, 30),  pos=(520, 380))
    self.btapp45 = wx.Button(painel, 30020,  "", size=(20, 30),  pos=(520, 350))


    self.Bind(wx.EVT_BUTTON,  self.Clicar,  id=10101)
    self.Show()

    def Clicar(self,  evt):
        pass

        if __name__ == '__main__':
                app = wx.App(False)
                frm1 = GameFrame(None,  wx.ID_ANY, "Batalha Naval", (750, 500))
                app.MainLoop()

