function g=pmc(f,ref,k,stepsize,nosteps,verbose,w,ip)
% Perona and Malik diffusion 

 if verbose
    figure(verbose);
    subplot(1,2,1);
    imshow(f);
    title('Original Image');
    drawnow;
 end
 g=f;
 [n,m]=size(f);
 N=n*m;

for i=1:nosteps
    
%     g=gD(g,0.001,0,0); % Apply this for Catte et al model
%     g=gD(g,0.4,0,0); % This is for linear diffusion model
     gx=gD(g,1,1,0);
     gy=gD(g,1,0,1);

    gpc=translateImage(g,1,0);
    gmc=translateImage(g,-1,0);
    gcp=translateImage(g,0,1);
    gcm=translateImage(g,0,-1);
    gpp=translateImage(g,1,1);
    gmp=translateImage(g,-1,1);
    gpm=translateImage(g,1,-1);
    gmm=translateImage(g,-1,-1);
   
   grad2=gx.*gx+gy.*gy;
   c=C(grad2);  
   
   %the following lines were added for eed model
   uscale = 1;
   Rx = gD(g,uscale,1,0);
   Ry = gD(g,uscale,0,1);
   Rw2 = Rx.^2+Ry.^2;
   Rw = sqrt(Rw2);
   c2 = C(Rw2);
   c1 = 1/5 * c2;
   
   dt_a = (c1.*Rx.^2+c2.*Ry.^2)./(Rw2+eps);
   dt_b = (c2-c1).*Rx.*Ry./(Rw2+eps);
   dt_c = (c1.*Ry.^2+c2.*Rx.^2)./(Rw2+eps);
   
   
   
   val=ip;
   switch val
       case 1
           % With  Weickert standard explicit scheme
%           g=g+stepsize*snldStep(g,c,w,ip); %applied for pm and pmc models
           g=g+stepsize*tnldStep(g,dt_a,dt_b,dt_c,ip); %applied for eed model
          
       otherwise disp('invalid choice');
   end
%end    %uncommented for linear diffusion model
     if verbose
        figure(verbose);
        subplot(1,2,2);
        imshow(g);
        title('Edge-enhancing Diffusion');
%        title('Linear Diffusion');
        drawnow;
     end
     u=g;
        
end %commented for linear diffusion model



