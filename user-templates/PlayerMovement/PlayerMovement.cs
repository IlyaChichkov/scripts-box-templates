using UnityEngine;

public class PlayerMovement : MonoBehaviour {
    
    private void Update() {

        var pos = transform.position;

        if(Input.GetKeyDown(KeyCode.W)){
            pos.y += 1;
        }
        if(Input.GetKeyDown(KeyCode.S)){
            pos.y -= 1;
        }
        if(Input.GetKeyDown(KeyCode.A)){
            pos.x += 1;
        }
        if(Input.GetKeyDown(KeyCode.D)){
            pos.x -= 1;
        }
        
        transform.position = pos;
    }
}