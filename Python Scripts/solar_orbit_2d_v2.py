G  = 6.67e-11
Mb = 4.0e30 # black hole
Ms = 2.0e30 # sun
Rs = 695700
AU = 1.5e11
daysec = 24.0*60*60

Planet = ['Mercurio', 'Venus', 'Tierra', 'Marte'] #, 'Jupiter', 'Saturno', 'Urano', 'Neptuno', 'Pluto']
Mass = [0.33010e24, 4.8673e24, 5.9722e24, 0.64169e24]
Aphelion_velocity =[38860, 34790, 29290, 21970]
Semimajor_axis = [0.38709893, 0.72333199, 1.00000011, 1.52366231]
Volumetric_mean_radius =[2439.7, 6051.8, 6371, 3389.5]

gravconst_mercurio = G * Mass[0] * Ms
gravconst_venus = G * Mass[1] * Ms
gravconst_tierra = G * Mass[2] * Ms
gravconst_marte = G * Mass[3] * Ms

# setup the starting conditions
#mercurio
xmercurio, ymercurio, zmercurio = Semimajor_axis[0] * AU, 0, 0
xvmercurio, yvmercurio, zvmercurio = 0, Aphelion_velocity[0], 0

#venus
xvenus, yvenus, zvenus = Semimajor_axis[1] * AU, 0, 0
xvvenus, yvvenus, zvvenus = 0, Aphelion_velocity[1], 0

# earth
xtierra, ytierra, ztierra = Semimajor_axis[2] * AU, 0, 0
xvtierra, yvtierra, zvtierra = 0, Aphelion_velocity[2], 0

# mars
xmarte, ymarte, zmarte = Semimajor_axis[3] * AU, 0, 0
xvmarte, yvmarte, zvmarte = 0, Aphelion_velocity[3], 0

# sun
xsol, ysol, zsol = 0, 0, 0
xvsol, yvsol, zvsol = 0, 0, 0

t = 0.0
dt = 1 * daysec # every frame move this time

xsollist, ysollist, zsollist = [], [], []
xmercuriolist, ymercuriolist, zmercuriolist = [], [], []
xvenuslist, yvenuslist, zvenuslist = [], [], []
xtierralist, ytierralist, ztierralist = [], [], []
xmartelist, ymartelist, zmartelist = [], [], []

# start simulation
while t < 2 * 365 * daysec:
    ################ mercury #############
    # compute G force on mercury
    rx_mercurio, ry_mercurio, rz_mercurio = xmercurio - xsol, ymercurio - ysol, zmercurio - zsol
    modr3_mercurio = (rx_mercurio ** 2 + ry_mercurio ** 2 + rz_mercurio ** 2) ** 1.5
    fx_mercurio = -gravconst_mercurio * rx_mercurio / modr3_mercurio
    fy_mercurio = -gravconst_mercurio * ry_mercurio / modr3_mercurio
    fz_mercurio = -gravconst_mercurio * rz_mercurio / modr3_mercurio
    
    # update quantities how is this calculated?  F = ma -> a = F/m
    xvmercurio += fx_mercurio * dt / Mass[0]
    yvmercurio += fy_mercurio * dt / Mass[0]
    zvmercurio += fz_mercurio * dt / Mass[0]
    
    # update position
    xmercurio += xvmercurio * dt
    ymercurio += yvmercurio * dt 
    zmercurio += zvmercurio * dt
    
    # save the position in list
    xmercuriolist.append(xmercurio)
    ymercuriolist.append(ymercurio)
    zmercuriolist.append(zmercurio)
    
    ################ Venus ##############
    # compute G force on venus
    rx_venus, ry_venus, rz_venus = xvenus - xsol, yvenus - ysol, zvenus - zsol
    modr3_venus = (rx_venus ** 2 + ry_venus ** 2 + rz_venus ** 2) ** 1.5
    fx_venus = -gravconst_venus * rx_venus / modr3_venus
    fy_venus = -gravconst_venus * ry_venus / modr3_venus
    fz_venus = -gravconst_venus * rz_venus / modr3_venus
    
    xvvenus += fx_venus * dt / Mass[1]
    yvvenus += fy_venus * dt / Mass[1]
    zvvenus += fz_venus * dt / Mass[1]
    
    # update position
    xvenus += xvvenus * dt
    yvenus += yvvenus * dt
    zvenus += zvvenus * dt
    
    # add to list
    xvenuslist.append(xvenus)
    yvenuslist.append(yvenus)
    zvenuslist.append(zvenus)
    
    ################ Earth #############
    # compute G force on earth
    rx, ry, rz = xtierra - xsol, ytierra - ysol, ztierra - zsol
    modr3_e = (rx ** 2 + ry ** 2 + rz ** 2) ** 1.5
    fx_tierra = -gravconst_tierra * rx / modr3_e
    fy_tierra = -gravconst_tierra * ry / modr3_e
    fz_tierra = -gravconst_tierra * rz / modr3_e
    
    # update quantities how is this calculated?  F = ma -> a = F/m
    xvtierra += fx_tierra * dt / Mass[2]
    yvtierra += fy_tierra * dt / Mass[2]
    zvtierra += fz_tierra * dt / Mass[2]
    
    # update position
    xtierra += xvtierra * dt
    ytierra += yvtierra * dt 
    ztierra += zvtierra * dt
    
    # save the position in list
    xtierralist.append(xtierra)
    ytierralist.append(ytierra)
    ztierralist.append(ztierra)
    
    ################ Mars ##############
    # compute G force on mars
    rx_marte, ry_marte, rz_marte = xmarte - xsol, ymarte - ysol, zmarte - zsol
    modr3_marte = (rx_marte ** 2 + ry_marte ** 2 + rz_marte ** 2) ** 1.5
    fx_marte = -gravconst_marte * rx_marte / modr3_marte
    fy_marte = -gravconst_marte * ry_marte / modr3_marte
    fz_marte = -gravconst_marte * rz_marte / modr3_marte
    
    xvmarte += fx_marte * dt / Mass[3]
    yvmarte += fy_marte * dt / Mass[3]
    zvmarte += fz_marte * dt / Mass[3]
    
    # update position
    xmarte += xvmarte * dt
    ymarte += yvmarte * dt
    zmarte += zvmarte * dt
    
    # add to list
    xmartelist.append(xmarte)
    ymartelist.append(ymarte)
    zmartelist.append(zmarte)
        
    ################ the sun ###########
    # update quantities how is this calculated?  F = ma -> a = F/m
    xvsol += -(fx_tierra + fx_marte) * dt / Ms
    yvsol += -(fy_tierra + fy_marte) * dt / Ms
    zvsol += -(fz_tierra + fz_marte) * dt / Ms
    
    # update position
    xsol += xvsol * dt
    ysol += yvsol * dt 
    zsol += zvsol * dt
    xsollist.append(xsol)
    ysollist.append(ysol)
    zsollist.append(zsol)
    
    # update dt
    t += dt

print('data ready')
#print(xalist,yalist)

import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib
matplotlib.rcParams['animation.embed_limit'] = 2**128
#matplotlib.use("TkAgg") # for mac M1
# from IPython.display import HTML

fig, ax = plt.subplots(figsize = (6, 6))
ax.set_aspect('equal')
ax.grid()

MarkerSizeSol = Rs / Volumetric_mean_radius[0]
MarkerSizeMercurio = Volumetric_mean_radius[0] / Volumetric_mean_radius[0]
MarkerSizeVenus = Volumetric_mean_radius[1] / Volumetric_mean_radius[0]
MarkerSizeTierra = Volumetric_mean_radius[2] / Volumetric_mean_radius[0]
MarkerSizeMarte = Volumetric_mean_radius[3] / Volumetric_mean_radius[0]

line_mercurio, = ax.plot([], [], '-g', lw = 1)
point_mercurio, = ax.plot([Semimajor_axis[0] * AU], [0], marker = "o", markersize = MarkerSizeMercurio, markeredgecolor = "blue", markerfacecolor = "blue")
text_mercurio = ax.text(Semimajor_axis[0] * AU, 0, 'Mercury')

line_venus, = ax.plot([], [], '-g', lw = 1)
point_venus, = ax.plot([Semimajor_axis[1] * AU], [0], marker = "o", markersize = MarkerSizeVenus, markeredgecolor = "blue", markerfacecolor = "blue")
text_venus = ax.text(Semimajor_axis[1] * AU, 0, 'Venus')

line_tierra, = ax.plot([], [], '-g', lw = 1)
point_tierra, = ax.plot([Semimajor_axis[2] * AU], [0], marker = "o", markersize = MarkerSizeTierra, markeredgecolor = "blue", markerfacecolor = "blue")
text_tierra = ax.text(Semimajor_axis[2] * AU, 0, 'Earth')

line_marte, = ax.plot([], [], '-g', lw = 1)
point_marte, = ax.plot([Semimajor_axis[3] * AU], [0], marker = "o", markersize = MarkerSizeMarte, markeredgecolor = "red", markerfacecolor = "red")
text_marte = ax.text(Semimajor_axis[3] * AU, 0, 'Mars')

point_sol, = ax.plot([0], [0], marker = "o", markersize = 7, markeredgecolor = "yellow", markerfacecolor = "yellow")
text_sol = ax.text(0, 0, 'Sun')

mercurioxdata, mercurioydata = [], [] # mercury track
venusxdata, venusydata = [], [] # venus track
tierraxdata, tierraydata = [], [] # earth track
martexdata, marteydata = [], [] # mars track
sxdata, sydata = [], [] # sun track

print(len(xtierralist))

def update(i):
    mercurioxdata.append(xmercuriolist[i])
    mercurioydata.append(ymercuriolist[i])
    
    venusxdata.append(xvenuslist[i])
    venusydata.append(yvenuslist[i])
    
    tierraxdata.append(xtierralist[i])
    tierraydata.append(ytierralist[i])
    
    martexdata.append(xmartelist[i])
    marteydata.append(ymartelist[i])
    
    line_mercurio.set_data(mercurioxdata, mercurioydata)
    point_mercurio.set_data(xmercuriolist[i], ymercuriolist[i])
    text_mercurio.set_position((xmercuriolist[i], ymercuriolist[i]))
    
    line_venus.set_data(venusxdata, venusydata)
    point_venus.set_data(xvenuslist[i], yvenuslist[i])
    text_venus.set_position((xvenuslist[i], yvenuslist[i]))
    
    line_tierra.set_data(tierraxdata, tierraydata)
    point_tierra.set_data(xtierralist[i], ytierralist[i])
    text_tierra.set_position((xtierralist[i], ytierralist[i]))
    
    line_marte.set_data(martexdata, marteydata)
    point_marte.set_data(xmartelist[i], ymartelist[i])
    text_marte.set_position((xmartelist[i], ymartelist[i]))
    
    point_sol.set_data(xsollist[i], ysollist[i])
    text_sol.set_position((xsollist[i], ysollist[i]))
    
    ax.axis('equal')
    ax.set_xlim(-2 * AU, 2 * AU)
    ax.set_ylim(-2 * AU, 2 * AU)
    #print(i)
    return (line_mercurio, line_venus, line_tierra, line_marte,
            point_mercurio, point_venus, point_tierra, point_marte,
            text_mercurio, text_venus, text_tierra, text_marte,
            point_sol, text_sol)

anim = animation.FuncAnimation(fig, func = update, frames = len(xmartelist), interval = 1, blit = True)
plt.show()

# from IPython.display import HTML
# HTML(anim.to_jshtml())