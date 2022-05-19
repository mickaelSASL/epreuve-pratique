/* debut */
unitsize(1cm);
defaultpen(fontsize(12));
settings.outformat="svg";

real larg = .5;
real haut = .7;
real epaiss = .6;


string tt(string texte) {
  return "\renewcommand*\ttdefault{txtt}\texttt{"+texte+"}";
}

void immeuble(int x, int h, int i, pen fond = invisible)
{
  filldraw(shift(((x-epaiss/2)*larg,0))*box((0,0),(epaiss*larg,h*haut)),fond, 1bp+grey);
  label(tt((string)i),(x*larg,0), S, fontsize(12pt)+grey);
  for (int j=1;j<h;++j)
  {
     draw(shift(((x-epaiss/2)*larg,j*haut))*((0,0)--(epaiss*larg,0)),1bp+grey);
  }
}

//int[] hauteurs = {1, 2, 1, 3, 4, 2, 5, 3, 1, 3};
int[] hauteurs = {2, 1, 2, 4, 0, 4, 5, 3, 5, 6};

draw((-larg,0)--(hauteurs.length*larg,0), grey);

/* couche 3 */

int hmax = 0;
for (int i=0;i<hauteurs.length;++i)
{
  pen fond = lightblue;
  while (hauteurs[i] > hmax)
  {  
     ++hmax;
     draw((-larg - 1, (hmax-.5)*haut) -- ((i-epaiss/2)*larg, (hmax-.5)*haut), orange+1.5bp, Arrow(TeXHead));
     fond = lightyellow;
  }   
  immeuble(i, hauteurs[i], i, fond);  
}

