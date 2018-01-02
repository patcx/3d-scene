#define MAX_LIGHTS 10

struct LightSource {
    vec4 position;
    vec4 spotDirection;
    float spotCutOff;
    float intensity;
};

uniform LightSource uLights[MAX_LIGHTS];

in vec4 v;
in vec3 n;
in vec3 fragDiffuse;

void main() 
{   
    float shininess = 30;
    vec3 finalColor = 0.2 * fragDiffuse;
    for(int i=0; i<MAX_LIGHTS; i++)
    {
        vec3 l = normalize(uLights[i].position - v);
        vec3 sd = normalize(-uLights[i].spotDirection);  
        vec3 V = normalize(-v); 
        vec3 r = normalize(reflect(l,n)); 

        if (dot(sd,l) > uLights[i].spotCutOff) 
        {
            vec3 Idiff = uLights[i].intensity * max(dot(n,l), 0.0) * fragDiffuse;
            Idiff = clamp(Idiff, 0.0, 1.0); 
            
            vec3  Ispec = pow(max(dot(r,V),0.0), shininess);
            Ispec= clamp(Ispec, 0.0, 1.0); 

            finalColor += Idiff + Ispec;
        }
    }

    gl_FragColor = vec4(finalColor, 1); 
}