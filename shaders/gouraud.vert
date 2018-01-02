#define MAX_LIGHTS 10

struct LightSource {
    vec4 position;
    vec4 spotDirection;
    float spotCutOff;
    float intensity;
};

uniform LightSource uLights[MAX_LIGHTS];

uniform int useBlinn;

uniform mat4 uModelMatrix;
uniform mat4 uViewMatrix;
uniform mat4 uProjectionMatrix;
uniform mat3 uNormalMatrix;

in vec4 position;
in vec3 normal;
in vec3 diffuse;

varying out vec3 color;


void main() 
{ 
    vec3 n = normalize(uNormalMatrix*normal);
    vec4 vertex = uModelMatrix * position;
    vec4 v = uViewMatrix * vertex;


    float shininess = 20;
    vec3 finalColor = 0.2 * diffuse;
    for(int i=0; i<MAX_LIGHTS; i++)
    {
        vec3 l = normalize(uLights[i].position - vertex);
        vec3 sd = normalize(-uLights[i].spotDirection);  
        vec3 V = normalize(-v); 
        vec3 r = normalize(reflect(l,n)); 
        vec3 H = normalize((l+v)/abs(l+v)); 

        if (dot(sd,l) > uLights[i].spotCutOff) 
        {
            vec3 Idiff = uLights[i].intensity * max(dot(n,l), 0.0) * diffuse;
            Idiff = clamp(Idiff, 0.0, 1.0); 
            vec3 Ispec;

            if(useBlinn)
                Ispec = pow(max(dot(n,H),0.0), shininess);
            else
                Ispec = pow(max(dot(r,V),0.0), shininess);

            Ispec= clamp(Ispec, 0.0, 1.0); 

            finalColor += Idiff + Ispec;
        }
    }

    color = clamp(finalColor, 0, 1);
    gl_Position = uProjectionMatrix * v;
}