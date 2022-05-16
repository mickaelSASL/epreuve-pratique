import math;
unitsize(1cm,1cm);

int[][] lab = {
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
    {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    {1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1},
    {1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    {1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1},
    {1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1},
    {1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1},
    {1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1},
    {1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1},
    {1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1},
    {1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1},
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
};

int i, j;
for(i=0; i<12; ++i){
    for(j=0; j<12; ++j){
        if(lab[i][j] == 1){
            path c = shift(j, 11 - i) * unitsquare;
            filldraw(c, deepgreen, black+2bp);
        }
    }
}
path c = shift(10.5, 1.5) * scale(0.4) * unitcircle;
filldraw(c, orange, black+2bp);
path c = shift(1.5, 10.5) * scale(0.4) * unitcircle;
filldraw(c, purple, black+2bp);

add(grid(12, 12, grey+2bp));

string[] chemin_1 = array('EEEEES');
string[] chemin_2 = array('SSSSSEENNNEEEEEEESSOOOOSSSEEEESS');


void chemine(string[] chemin, int l, pen p){
    real x = 1 + 0.5;
    real y = 12 - 1 - 0.5;
    int k = 0;
    for(int k=0; k<l; ++k){
        if        (chemin[k] == 'N'){
            draw((x, y)--(x, y+1), p, Arrow(HookHead, 5bp));
            ++y;
        } else if (chemin[k] == 'S'){
            draw((x, y)--(x, y-1), p, Arrow(HookHead, 5bp));
            --y;
        } else if (chemin[k] == 'E'){
            draw((x, y)--(x+1, y), p, Arrow(HookHead, 5bp));
            ++x;
        } else if (chemin[k] == 'O'){
            draw((x, y)--(x-1, y), p, Arrow(HookHead, 5bp));
            --x;
        }
    }
}

draw(shift(6.5, 9.5)*scale(0.3)*cross(4, round=true, r=0.1), black+6bp);
chemine(chemin_1, 6, red+2bp);
chemine(chemin_2, 32, lightblue+2bp);

label("N", ( 6, 12), 2*N, fontsize(32pt)+gray);
label("E", (12,  6), 2*E, fontsize(32pt)+gray);
label("S", ( 6,  0), 2*S, fontsize(32pt)+gray);
label("O", ( 0,  6), 2*W, fontsize(32pt)+gray);


shipout(bbox(.25cm));
